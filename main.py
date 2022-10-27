from webcommand import Web
from mp4_mp3 import mp4_mp3

test = True

def main():

    if test:
        web = Web()

        web.quit()
        
        web.test_url()
    
    else:
        web = Web()

        a = input()

        web.quit()

    web.download()

    mp4_mp3().all()

    


if __name__ == "__main__":
    main()
