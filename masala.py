a = input('''
Sizga qaysi maishiy texnika kerak:
          1==televizor
          2==konditsioner
          3==muzlatgich
          ''')


tehnika = {
    'televizor':{
        't1':['Artel','qora','oq','qizil',1212323],
        't2':['Samsung','qora','oq','qizil',235666],
        't3':['Shivaki','qora','oq','qizil',2346]
    },
    'konditsioner':{
        'k1':['artel','qora','oq','qizil',100000],
        'k2':['samsung','qora','oq','qizil',235666],
        'k3':['shivaki','qora','oq','qizil',2346]
    },
    'muzlatgich':{
        'm1':['artrel','qora','oq','qizil',1212323],
        'm2':['samsung','qora','oq','qizil',235666],
        'm3':['shivaki','qora','oq','qizil',2346]
    }
}
if a=='1':
    print('tabriklaymiz, siz televizor bo\'limni tanladingiz')
    print(tehnika['televizor']['t1'][0],tehnika['televizor']['t2'][0],tehnika['televizor']['t3'][0])
    
    b=input('''sizga qaysi kompaniya mahsuloti kerak:
      ''')
    if b.lower()=='artel':
        print('siz',tehnika['televizor']['t1'][0],'kompaniyasini tanladingiz')
        c=input('sizga qaysi rangdagisi kerak:   ')
        if c.lower()=='oq':
            print('siz',tehnika['televizor']['t1'][2],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['t1'][4],'so\'m')
        elif c.lower()=='qora':
             print('siz',tehnika['televizor']['t1'][1],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['t1'][4],'so\'m')
        elif c.lower()=='qizil':
            print('siz',tehnika['televizor']['t1'][3],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['t1'][4],'so\'m')

    elif b.lower()=='samsung':
        print('siz',tehnika['televizor']['t2'][0],'kompaniyasini tanladingiz')
        c=input('sizga qaysi rangdagisi kerak:   ')
        if c.lower()=='oq':
            print('siz',tehnika['televizor']['t2'][2],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['t2'][4],'so\'m')
        elif c.lower()=='qora':
            print('siz',tehnika['televizor']['t2'][1],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['t2'][4],'so\'m')
        elif c.lower()=='qizil':
            print('siz',tehnika['televizor']['t2'][3],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['t2'][4],'so\'m')

    elif b.lower()=='shivaki':
        print('siz',tehnika['televizor']['t3'][0],'kompaniyasini tanladingiz')
        c=input('sizga qaysi rangdagisi kerak:   ')
        if c.lower()=='oq':
            print('siz',tehnika['televizor']['t3'][2],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['t3'][4],'so\'m')
        elif c.lower()=='qora':
            print('siz',tehnika['televizor']['t3'][1],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['t3'][4],'so\'m')
        elif c.lower()=='qizil':
            print('siz',tehnika['televizor']['t3'][3],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['t3'][4],'so\'m')
    


elif a=='2':
    print('tabriklaymiz, siz konditsioner bo\'limni tanladingiz')
    print(tehnika['konditsioner']['k1'][0],tehnika['konditsioner']['k2'][0],tehnika['konditsioner']['k3'][0])
    
    b=input('''sizga qaysi kompaniya mahsuloti  kerak:
      ''')
    if b.lower()=='artel':
        print('siz',tehnika['konditsioner']['k1'][0],'kompaniyasini tanladingiz')
        c=input('sizga qaysi rangdagisi kerak:   ')
        if c.lower()=='oq':
            print('siz',tehnika['konditsioner']['k1'][2],'ranglisini tanladingiz , uning narxi',tehnika['konditsioner']['k1'][4],'so\'m')
        elif c.lower()=='qora':
            print('siz',tehnika['konditsioner']['k1'][1],'ranglisini tanladingiz , uning narxi',tehnika['konditsioner']['k1'][4],'so\'m')
        elif c.lower()=='qizil':
            print('siz',tehnika['konditsioner']['k1'][3],'ranglisini tanladingiz , uning narxi',tehnika['konditsioner']['t1'][4],'so\'m')

    elif b.lower()=='samsung':
        print('siz',tehnika['konditsioner']['k2'][0],'kompaniyasini tanladingiz')
        c=input('sizga qaysi rangdagisi kerak:   ')
        if c.lower()=='oq':
            print('siz',tehnika['konditsioner']['k2'][2],'ranglisini tanladingiz , uning narxi',tehnika['konditsioner']['k2'][4],'so\'m')
        elif c.lower()=='qora':
            print('siz',tehnika['konditsioner']['k2'][1],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['k2'][4],'so\'m')
        elif c.lower()=='qizil':
            print('siz',tehnika['konditsioner']['k2'][3],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['k2'][4],'so\'m')


    elif b.lower()=='shivaki':
        print('siz',tehnika['konditsioner']['k3'][0],'kompaniyasini tanladingiz')
        c=input('sizga qaysi rangdagisi kerak:   ')
        if c.lower()=='oq':
            print('siz',tehnika['konditsioner']['k3'][2],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['k3'][4],'so\'m')
        elif c.lower()=='qora':
            print('siz',tehnika['konditsioner']['k3'][1],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['k3'][4],'so\'m')
        elif c.lower()=='qizil':
            print('siz',tehnika['konditsioner']['k3'][3],'ranglisini tanladingiz , uning narxi',tehnika['televizor']['k3'][4],'so\'m')
    


elif a=='3':
    print('tabriklaymiz, siz muzlatgich bo\'limni tanladingiz')
    print(tehnika['muzlatgich']['m1'][0],tehnika['muzlatgich']['m2'][0],tehnika['muzlatgich']['m3'][0])
    
    b=input('''sizga qaysi kompaniya mahsuloti  kerak:
      ''')
    if b.lower()=='artel':
        print('siz',tehnika['muzlatgich']['m1'][0],'kompaniyasini tanladingiz')
        c=input('sizga qaysi rangdagisi kerak:   ')
        if c.lower()=='oq':
            print('siz',tehnika['muzlatgich']['m1'][2],'ranglisini tanladingiz , uning narxi',tehnika['muzlatgich']['m1'][4],'so\'m')
        elif c.lower()=='qora':
            print('siz',tehnika['muzlatgich']['m1'][1],'ranglisini tanladingiz , uning narxi',tehnika['muzlatgich']['m1'][4],'so\'m')
        elif c.lower()=='qizil':
            print('siz',tehnika['muzlatgich']['m1'][3],'ranglisini tanladingiz , uning narxi',tehnika['muzlatgich']['m1'][4],'so\'m')


    elif b.lower()=='samsung':
        print('siz',tehnika['muzlatgich']['m2'][0],'kompaniyasini tanladingiz')
        c=input('sizga qaysi rangdagisi kerak:   ')
        if c.lower()=='oq':
            print('siz',tehnika['muzlatgich']['m2'][2],'ranglisini tanladingiz , uning narxi',tehnika['muzlatgich']['m2'][4],'so\'m')
        elif c.lower()=='qora':
            print('siz',tehnika['muzlatgich']['m2'][1],'ranglisini tanladingiz , uning narxi',tehnika['muzlatgich']['m2'][4],'so\'m')
        elif c.lower()=='qizil':
            print('siz',tehnika['muzlatgich']['m2'][3],'ranglisini tanladingiz , uning narxi',tehnika['muzlatgich']['m2'][4],'so\'m')


    elif b.lower()=='shivaki':
        print('siz',tehnika['muzlatgich']['m3'][0],'kompaniyasini tanladingiz')
        c=input('sizga qaysi rangdagisi kerak:   ')
        if c.lower()=='oq':
            print('siz',tehnika['muzlatgich']['m3'][2],'ranglisini tanladingiz , uning narxi',tehnika['muzlatgich']['m3'][4],'so\'m')
        elif c.lower()=='qora':
            print('siz',tehnika['muzlatgich']['m3'][1],'ranglisini tanladingiz , uning narxi',tehnika['muzlatgich']['m3'][4],'so\'m')
        elif c.lower()=='qizil':
            print('siz',tehnika['muzlatgich']['m3'][3],'ranglisini tanladingiz , uning narxi',tehnika['muzlatgich']['m3'][4],'so\'m')


    
