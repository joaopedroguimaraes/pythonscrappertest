import re

import lxml.html.clean as clean
import scrapy

from ..items import ContactItem


def sanitize_phone_number(phone_text):
    sanitized = []
    ignore_characters = ['(', ')', '+']
    for character in phone_text.strip():
        if not character.isdigit():
            if character not in ignore_characters:
                sanitized.append(' ')
            else:
                sanitized.append(character)
        else:
            sanitized.append(character)
    return ''.join(sanitized)


def find_phones(response_body):
    pattern = r'(?:[+]\d{1,2}|) {0,1}[(]{0,1}\d{1,3}[)]{0,1} {0,1}\d{3,4}(?:[-]| |)(?:\d{4}|\d{2}[-]\d{2})'
    phones_matches = [sanitize_phone_number(match) for match in re.findall(pattern, response_body)]
    phones = []
    for new_phone in phones_matches:
        if new_phone not in phones:
            phones.append(new_phone)
    return phones


def find_logo(url_request, response_body_selector):
    base_url = '/'.join(url_request.split('/')[:3]).lower()
    images = response_body_selector.xpath('.//img')
    for image in images:

        attributes = image.attrib
        if 'class' in attributes and 'logo' in attributes['class'].lower() \
                or 'logo' in attributes['src'].lower():
            if '.com' in image.attrib['src']:
                if image.attrib['src'][:2] == '//':
                    return f"http:{image.attrib['src']}"
                else:
                    return f"http://{image.attrib['src']}"
            elif base_url in image.attrib['src']:
                return image.attrib['src']
            else:
                return f"{base_url}{image.attrib['src']}"


def clean_response_body(response_body):
    safe_attrs = {}
    cleaner = clean.Cleaner(safe_attrs_only=True, safe_attrs=safe_attrs, scripts=True)

    return cleaner.clean_html(response_body)


class ContactInfoSpider(scrapy.Spider):
    name = 'contactinfo'

    def parse(self, response, **kwargs):
        response_body_selector = response.xpath('//body')
        response_text = clean_response_body(response_body_selector.extract_first())
        contact_info = ContactItem()
        contact_info['phones'] = find_phones(response_text)
        contact_info['logo_url'] = find_logo(response.url, response_body_selector[0])
        contact_info['url'] = response.url
        yield contact_info
