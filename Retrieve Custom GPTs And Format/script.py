import openai

# Replace 'your_openai_api_key' with your actual OpenAI API key
openai.api_key = 'your_openai_api_key'

def get_custom_gpts():
    response = openai.Engine.list()  # Retrieve the list of engines
    return response['data']

def format_gpts_to_table(gpts):
    table = []
    for gpt in gpts:
        if 'fine-tuned' in gpt['id']:  # Filter out only custom/fine-tuned models
            name = gpt['id']
            url = f"https://platform.openai.com/engines/{name}"
            table.append({'Script Name': name, 'Script URL': url})
    return table

def print_table(table):
    header = table[0].keys()
    rows = [x.values() for x in table]
    column_widths = [max(len(str(item)) for item in column) for column in zip(*[header] + rows)]
    format_str = ' | '.join(f'{{:<{width}}}' for width in column_widths)
    print(format_str.format(*header))
    print('-' * sum(column_widths) + '-' * (len(column_widths) - 1))
    for row in rows:
        print(format_str.format(*row))

if __name__ == "__main__":
    custom_gpts = get_custom_gpts()
    table = format_gpts_to_table(custom_gpts)
    if table:
        print_table(table)
    else:
        print("No custom GPTs found.")
