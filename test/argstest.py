import sys
def main_async(args):
    print(len(args))
    def genData(args):
        result = {}
        if len(args) >= 2:
            arr = []
            for arg in args:
                if ('purge=' in arg) or (',' in arg):
                    if 'purge=' in arg:
                        result['purge'] = True if arg.split('purge=')[1].lower() == 'true' else False
                    else:
                        s = arg.split(',')
                        if len(s) >= 2:
                            temp = {}
                            temp['source'] = s[0]
                            temp['target'] = s[1]
                            arr.append(temp)
            result['data'] = arr
        return result
    print(genData(args))

if __name__ == '__main__':
    main_async(sys.argv)