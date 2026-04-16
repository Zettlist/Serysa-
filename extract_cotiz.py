
h=open('index.html',encoding='utf-8').read()
i = h.find('class="cotiz-options"')
if i == -1:
    open('cotiz_chunk.txt','w',encoding='utf-8').write("NOT FOUND")
else:
    open('cotiz_chunk.txt','w',encoding='utf-8').write(h[i:i+2500])
print("done")

