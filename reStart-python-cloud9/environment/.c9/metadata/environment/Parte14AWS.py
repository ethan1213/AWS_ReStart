{"filter":false,"title":"Parte14AWS.py","tooltip":"/Parte14AWS.py","undoManager":{"mark":23,"position":23,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":2},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":3},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["j"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["s"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["o"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["n"]}],[{"start":{"row":0,"column":11},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":4}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["d"],"id":5},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["e"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":[" "],"id":6},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["r"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["e"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["a"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["d"]}],[{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["J"],"id":7},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["s"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["o"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["n"]}],[{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["F"],"id":8},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["i"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["l"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":16},"end":{"row":1,"column":18},"action":"insert","lines":["()"],"id":9}],[{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["f"],"id":10},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["i"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["l"]},{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":["N"],"id":11},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["a"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["m"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["e"]}],[{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":[":"],"id":12}],[{"start":{"row":1,"column":27},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":2,"column":0},"end":{"row":2,"column":3},"action":"insert","lines":["   "]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["d"]},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":["a"]},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["t"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["a"]}],[{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["="],"id":14}],[{"start":{"row":2,"column":8},"end":{"row":2,"column":10},"action":"insert","lines":["\"\""],"id":15}],[{"start":{"row":2,"column":10},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":3,"column":0},"end":{"row":3,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":3,"column":3},"end":{"row":5,"column":15},"action":"insert","lines":["with open('files/insulin.json') as json_file:","        data = json.load(json_file)","    return data"],"id":17}],[{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"remove","lines":["n"],"id":18}],[{"start":{"row":1,"column":0},"end":{"row":5,"column":15},"action":"remove","lines":["def readJsonFile(fileName):","   data=\"\"","   with open('files/insuli.json') as json_file:","        data = json.load(json_file)","    return data"],"id":19},{"start":{"row":1,"column":0},"end":{"row":8,"column":15},"action":"insert","lines":["def readJsonFile(fileName):","    data = \"\"","    try:","        with open(fileName) as json_file:","            data = json.load(json_file)","    except IOError:","        print(\"Could not read file\")","    return data"]}],[{"start":{"row":0,"column":11},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":20}],[{"start":{"row":0,"column":11},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":21}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["import jsonFileHandler",""],"id":22}],[{"start":{"row":11,"column":15},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"insert","lines":["    "]},{"start":{"row":12,"column":4},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"remove","lines":[" "],"id":24},{"start":{"row":13,"column":0},"end":{"row":13,"column":3},"action":"remove","lines":["   "]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":22},"action":"remove","lines":["import jsonFileHandler"],"id":30},{"start":{"row":0,"column":11},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":11},"end":{"row":0,"column":11},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":7,"state":"start","mode":"ace/mode/python"}},"timestamp":1732904762128,"hash":"878465143d52bcea737e043cacd8cea1d1a12bbf"}