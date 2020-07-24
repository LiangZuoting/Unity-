import urllib

urlformatstr = 'http://fixbyproximity.com/Downloads/Hour_{0}_Files.zip'
destfilenameformatstr = 'Hour_{0}_Files.zip'
numformatstr = '{:0>2d}'
for i in range(1, 24):
    print('downloading ' + str(i))
    numstr = numformatstr.format(i)
    url = urlformatstr.format(numstr)
    destfilename = destfilenameformatstr.format(numstr)
    urllib.urlretrieve(url, destfilename)
    print('done')

print('all done')
