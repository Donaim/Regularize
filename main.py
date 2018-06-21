
import window
import file_manager
import cmap
import updater
import cli
import rules

def main():
    print('Hello!')

    u = cli.Parser()
    
    fname = file_manager.create_temp()
    p = file_manager.open_file('/usr/bin/gedit', fname)

    def check(): return (p.returncode is None) and (not u._forse_exit)
    def callback(): 
        bma = updater.load_map(fname)
        window.update_map_bool(bma)

        if not bma is None:
            if cmap.equal_q(bma, u._current_bmap):
                print ('match    :)', end = ' ')
            else:
                print ('no match :(', end = ' ')
            print ('tokens={}'.format(rules.count_tokens_from_file(fname)))

    file_manager.listen_file(fname, check, callback)

    window.show()
    u.reload()
    u._parse_loop()

    window.close()
    p.kill()
    
    print('Bye!')

if __name__ == '__main__':
    main()

