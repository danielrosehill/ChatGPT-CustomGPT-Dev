# Explanation:

Retrieve Custom GPTs:

The get_custom_gpts function calls the OpenAI API to list all engines and returns them.
Format to Table:

The format_gpts_to_table function filters out the custom fine-tuned models (you can adjust the filtering condition based on your naming conventions or attributes) and formats them into a table format with 'Script Name' and 'Script URL' columns.
Print Table:

The print_table function prints the table in a readable format.

# Important Notes:

Ensure you replace 'your_openai_api_key' with your actual OpenAI API key.

The filtering condition 'fine-tuned' in gpt['id'] is based on a common naming pattern for fine-tuned models. Adjust this condition as needed to match your actual custom GPT IDs.

This script assumes that the custom GPT IDs contain 'fine-tuned'. Modify the filtering logic if your custom model IDs follow a different pattern.