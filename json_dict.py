import json
import glob

def hiji_jsonload(jasondirname="dirname"):
    #jason_dirname >> "/home/user/mimura/input/train_anns"

    filename = sorted(glob.glob("{}/*.json".format(jasondirname)))
    bboxes = []

    for ii in range(len(filename)):
        with open(filename[ii]) as f:
            df = json.load(f)

        char = []
        xmin = []
        ymin = []
        xmax = []
        ymax = []

        for i in range(len(df["bboxes"])):
            char.append(df["bboxes"][i]["char"])
            xmin.append(df["bboxes"][i]["xmin"])
            ymin.append(df["bboxes"][i]["ymin"])
            xmax.append(df["bboxes"][i]["xmax"])
            ymax.append(df["bboxes"][i]["ymax"])

        bboxes.append([char,xmin,ymin,xmax,ymax,df["label"]])

    return bboxes