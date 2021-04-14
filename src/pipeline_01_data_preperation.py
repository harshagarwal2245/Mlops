import os,argparse,yaml,logging

def read_config(config_path):
    """read configration file function 
    Input: Path for configuration files
    Output: Configuration output dictionary"""
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    
    return config


def main(config_path,data_source):
    """Main entry to code 
    Input paths to data source and config file"""
    config=read_config(config_path)
    print(config)



if __name__=="__main__":
    args=argparse.ArgumentParser()
    default_config_path=os.path.join("config","params.yaml")
    args.add_argument("--config",default=default_config_path)
    args.add_argument("--datasource",default=None)
    parsed_arg=args.parse_args()
    main(config_path=parsed_arg.config,data_source=parsed_arg.datasource)

    
