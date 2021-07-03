import base64
nsfw='fuck'
ans=base64.b64encode(nsfw.encode())
print(ans.decode())
# ZnVjaw==
test=base64.b64decode(ans).decode()
print(test)
# fuck
