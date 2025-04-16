import devfx.config as cfg

if __name__ == '__main__':
    cfg.Configuration.load('devfx_samples/config/config.json')

    section1 = cfg.Configuration.get('section1')
    print(section1['value1'])
    print(section1['value2'])

    value111 = cfg.Configuration.get('section1:section11:value111')
    print(value111)

