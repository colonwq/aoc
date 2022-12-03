    for item in missing:
        item_ord = ord(item)
#        print("Pre-Missing item: %s(%d)" %( item, item_ord) )
        if item_ord >=97 and item_ord <= 122:
#            print("Lower case %d"%(item_ord))
            item_ord-=96
        elif item_ord >= 65 and item_ord <= 90:
#            print("Before Upper case %d"%(item_ord))
            item_ord = item_ord-38
#            print("--------AFTER Upper case %d"%(item_ord))
#        print("Missing item: %s(%d)" %( item, item_ord) )
        answer += item_ord
