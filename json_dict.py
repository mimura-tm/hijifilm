import jason
import globe
import os


def hiji_jsonload():
    for ii in range():
        with open(json) as f:
            df = jason.load(f)

        bboxes = []
        char = []
        xmin = []
        ymin = []
        xmax = []
        ymax = []
        label = []

        for i in range(len(df["bboxes"])):
            char.append(df["bboxes"][i]["char"])
            xmin.append(df["bboxes"][i]["xmin"])
            ymin.append(df["bboxes"][i]["ymin"])
            xmax.append(df["bboxes"][i]["xmax"])
            ymax.append(df["bboxes"][i]["ymax"])

        bboxes.append([char,xmin,ymin,xmax,ymax,df["label"]])

def hiji_jsonload2(jasondirname):
    filename = sorted(globe.globe("*/{}/*.jason".format(jasondirname)))
    bboxes = []

    for ii in range():
        with open(jason) as f:
            df = jason.load(f)

        char = []
        xmin = []
        ymin = []
        xmax = []
        ymax = []
        label = []

        for i in range(len(df["bboxes"])):
            char.append(df["bboxes"][i]["char"])
            xmin.append(df["bboxes"][i]["xmin"])
            ymin.append(df["bboxes"][i]["ymin"])
            xmax.append(df["bboxes"][i]["xmax"])
            ymax.append(df["bboxes"][i]["ymax"])

        bboxes.append([char,xmin,ymin,xmax,ymax,df["label"]])