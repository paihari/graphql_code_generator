import os
import argparse
import graphene
from graphql import build_ast_schema, parse

def generate_python_code(schema_file_path, output_dir):
    # Read the schema definition from the file
    with open(schema_file_path, 'r') as f:
        schema_definition = f.read()

    # Use graphql library to build AST-based schema
    ast_schema = build_ast_schema(parse(schema_definition))

    # Use Graphene to generate Python types and resolvers based on your schema
    schema = graphene.Schema.from_ast(ast_schema)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate a separate Python file for each type in the schema
    for type_name, graphql_type in ast_schema.type_map.items():
        if graphql_type.name.startswith('__'):
            continue
        type_file = os.path.join(output_dir, type_name.lower() + '.py')
        with open(type_file, 'w') as f:
            f.write(f'# Add your business logic for {type_name} here\n')
            f.write('from generated_code.mutation import Mutation\n\n')
            f.write(f'class {type_name}Resolver:\n')
            for field_name, field_definition in graphql_type.fields.items():
                arg_str = ', '.join([f'{arg.name}: {arg.type}' for arg in field_definition.args])
                f.write(f'    def resolve_{field_name}(self, info, {arg_str}):\n')
                f.write(f'        # Add your business logic here\n')
                f.write(f'        return None\n\n')
            f.write('mutation = Mutation.Field()\n\n')
            f.write('# Define your GraphQL schema using the generated resolvers\n')
            f.write('schema = graphene.Schema(query=query_type, mutation=mutation_type)\n')

    # Print a confirmation message
    print(f'Python code generated and saved to directory {output_dir}.')


def main():
    # Define command-line arguments
    parser = argparse.ArgumentParser(description='Generate Python code based on a GraphQL schema file.')
    parser.add_argument('schema_file', help='Path to the GraphQL schema file.')
    parser.add_argument('-o', '--output-dir', help='Path to the directory where the generated Python code should be saved. Default is "./generated_code".', default='./generated_code')

    # Parse command-line arguments
    args = parser.parse_args()

    # Generate Python code from the schema file
    generate_python_code(args.schema_file, args
