# by Kami Bigdely
# Remove control flag
# Reference: https://stackoverflow.com/a/10140333/81306
# This code snippet reads up to the end of the file
n = 16
with open('foobar.file', 'rb') as fp:
    while True:
        chunk = fp.read(n)
        if chunk == '': # end of file, stop running.
            return
        else:
            print(chunk)
        # process(chunk)
