import argparse

from .scripts import mk_draft, mk_site, edit, build, deploy

def main():
    parser = argparse.ArgumentParser(
        prog='penguin',
        description='Generador de sitios estaticos'
    )
    
    subparser = parser.add_subparsers(dest='command', help='Comandos disponibles')
   
    # Comando new
    new_parser = subparser.add_parser("new", help='Crea un nuevo sito o post')
    new_parser.add_argument("type", choices=['site', 'post'], help='Accion a realizar')
    new_parser.add_argument("name", help='Nombre del sitio o post')

    # Comando edit
    edit_parser = subparser.add_parser("edit", help='Busca post por el titulo para editarlo')
    edit_parser.add_argument('query', help='titulo del post')
    
    # Comando build y deploy
    subparser.add_parser("build", help='Construye el sitio')
    subparser.add_parser("deploy", help='Deploya el sitio')
    
    args = parser.parse_args()
    
    
    # Logica segun comando
    if args.command == 'new':
        if args.type == 'site':
            mk_site.create_site(args.name)
        elif args.type == 'post':
            mk_draft.create_draft(args.name)
    elif args.command == 'edit':
        if args.query:
            edit.edit_draft(args.query)
    elif args.command == 'build':
        build.build()
    elif args.command == 'deploy':
        deploy.deploy_to_github()
