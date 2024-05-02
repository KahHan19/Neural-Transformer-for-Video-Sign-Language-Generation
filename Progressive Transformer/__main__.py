import argparse
import sys
from training import train, test
from os import listdir
from os.path import isfile, join

def main():

    # Example options:
    # train ./Configs/Base.yaml
    # test ./Configs/Base.yaml
    # path="./Configs/furtherGlossConfigs"
    # path="./Configs/configs"
    # files = [path+"/"+f for f in listdir(path) if isfile(join(path, f))]
    # print(files)
    # configs = files
    # print(configs)
    # ap = argparse.ArgumentParser("Progressive Transformers")
    # ap.add_argument("mode", choices=["train", "test"],
    #                 help="train a model or test")
    # ap.add_argument("config_path", type=str,
    #                 help="path to YAML config file")
    # ap.add_argument("--ckpt", type=str,
    #                 help="path to model checkpoint")
    # args = ap.parse_args()
    # for i in configs:
    #     args.config_path=i
    #     # # If Train
    #     # if args.mode == "train":
    #     train(cfg_file=args.config_path, ckpt=args.ckpt)
        # # If Test
        # elif args.mode == "test":
        #     test(cfg_file=args.config_path, ckpt=args.ckpt)
        # else:
        #     raise ValueError("Unknown mode")
    
    # train(cfg_file=args.config_path, ckpt=args.ckpt)


    # test(cfg_file=args.config_path, ckpt=args.ckpt)

    ap = argparse.ArgumentParser("Progressive Transformers")
    
    # Choose between Train and Test
    ap.add_argument("mode", choices=["train", "test"],
                    help="train a model or test")
    # Path to Config
    ap.add_argument("config_path", type=str,
                    help="path to YAML config file")
    ap.add_argument("--ckpt", type=str,
                    help="path to model checkpoint")
    
    args = ap.parse_args()

    if args.mode == "train":
        print("here")
        print("test")
        train(cfg_file=args.config_path)
    elif args.mode == "test":
        test(cfg_file=args.config_path, ckpt=args.ckpt)
    else:
        raise ValueError("Unknown mode")

    # path="./Models/testing/sign_data"
    # path2="./Models/testing/further_v2"
    # processed_files = [f for f in listdir(path2)]
    # configs = [path+"/"+f+"/config.yaml" for f in listdir(path) if f not in processed_files]
    # for i in configs:
    #     train(cfg_file=i)
    
    # path="./Models/testing/further_v2"
    # configs = [path+"/"+f+"/config.yaml" for f in listdir(path) if "text_vocab" in f]
    # # for count, i in enumerate(configs):
    # #     if "text_vocab.txt_2_8_(256, 512)" in i:
    # #         print(count)
    # for i in configs:
    #     test(cfg_file=i, ckpt=None)

    # config_path = "./Models/testing/sign_data/gloss_vocab.txt_1_8_(512, 1024)/config.yaml"
    # # ckpt = "Models/testing/further_v2/text_vocab.txt_1_8_(512, 1024)/27000_best.ckpt"
    # test(cfg_file=config_path, ckpt=None)

if __name__ == "__main__":
    main()
