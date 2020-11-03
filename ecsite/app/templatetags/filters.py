from django import template

register = template.Library()


@register.simple_tag  # シンプルな構成のテンプレートタグを作成する時に利用
def multiply(value1, value2):
    return value1 * value2
