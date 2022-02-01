from lib.check_ssl_domains import DomainTools
import sys
import argparse

def arguments():
    parser = argparse.ArgumentParser(description='check SSL domains.')
    parser.add_argument('-D', '--insert-to-database', help='Insert data into database',
                action='store_true')
    
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    
    args_dict = vars(args)

    # Get domains info and insert into database
    if args_dict['insert_to_database']:
        DomainTools().insert_data_to_db()
        sys.exit(0)
    
if __name__ == '__main__':
    arguments()
