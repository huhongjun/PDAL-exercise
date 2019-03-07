ccode = [6, 16, 2, 5, 14, 3, 4, 8, 12, 17]
cname = ['buildings','conductor','ground','high_vegetation','lake','low_vegetation','mid_vegetation','mkp_ground','road','structures']
folder = "cz_1-9"

import pdal

for i in range(2) :
    code = ccode[i]
    name = folder +'_'+ cname[i]
    json =  """{
  "pipeline": [
      {
            "type" : "readers.las",
            "filename" : "cz_1-9\\\\input\\\\%s.las"
      },
      {
          "type" : "filters.assign",
          "assignment" : "Classification[0:32]=%s"
      },
      {
          "type" : "writers.text",
          "format": "csv",
          "order":"X,Y,Z,PointSourceId,ScanAngleRank,ScanDirectionFlag,NumberOfReturns,ReturnNumber,Intensity,Classification",
          "keep_unspecified":"false",          
          "filename" : "cz_1-9\\\\output\\\\%s.csv"
      }
  ]
}""" % (name,code,name)
    pipeline = pdal.Pipeline(json)
    pipeline.validate() # check if our JSON and options were good
    pipeline.loglevel = 8 #really noisy
    count = pipeline.execute()
    print(" - Code: %s, Name: %s, Count: %s " % (code,name,count))