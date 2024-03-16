import subprocess

#hash: 0cbab7e743096d327e14367134b9873a

class hashcat_api():
    def crack(hash_mode:int,attack_mode:int,hash:str):
        process = subprocess.Popen(["hashcat",f"-m{hash_mode}",f"-a{attack_mode}",hash],stdout=subprocess.PIPE)
        return process.stdout.read().decode("utf-8").strip()
    def show_potfile(hash):
        process = subprocess.Popen(["hashcat","-m0",hash,"--show"],stdout=subprocess.PIPE)
        return process.stdout.read().decode("utf-8").strip()
