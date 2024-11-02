import re

class Extractor:
    @staticmethod
    def extract_fabric_from_description(description):
        if description is not None and description.text is not None:
            match = re.search(r'<strong>Kumaş Bilgisi:</strong>(.*?)</li>', description.text)
            if match:
                return match.group(1).replace('&nbsp;', '').strip()
        return ""

    @staticmethod
    def extract_model_measurements(description):
        if description is not None and description.text is not None:
            match = re.search(r'<strong>Model Ölçüleri:</strong>(.*?)</li>', description.text)
            if match:
                return match.group(1).replace('&nbsp;', '').strip()
        return ""

    @staticmethod
    def extract_product_measurements(description):
        if description is not None and description.text is not None:
            match = re.search(r'<strong>Ürün Ölçüleri:</strong>(.*?)</li>', description.text) or re.search(r'<strong>Ürün Ölçüleri1:</strong>(.*?)</li>', description.text)

            if match:
                return match.group(1).replace('&nbsp;', '').strip()
        return ""

    @staticmethod
    def extract_product_information(description):
        if description is not None and description.text is not None:
            product_info_match = re.search(r'<strong>Ürün Bilgisi:</strong>(.*?)<strong>Kumaş Bilgisi:</strong>', description.text) or re.search(r'<strong>Ürün Bilgisi: </strong>(.*?)</li>', description.text)
            if product_info_match:
                product_info = product_info_match.group(1).replace('&nbsp;', '').strip()
                additional_info = re.findall(r'(\bModelin üzerindeki ürün\b.*?\<li\>)', description.text)
                if additional_info:
                    product_info += ', ' + additional_info[0].replace('&nbsp;', '').strip()
                
                product_info = re.sub(r'<.*?>', '', product_info)  # Clean HTML tags
                return product_info.strip()
        return ""
