# example/simple/views.py

from django.http import HttpResponse
from frames.models import Frame, Block
import re

def home(request):
    # Create links and OpenID form to the Login handler.
    return HttpResponse('''
        Welcome to Timeline(long123king@163.com)!
    ''')

def frame_by_index(request, index):
    frames = Frame.objects.filter(id = index)
    if len(frames) == 0:
	    return HttpResponse("Invalid index : " + index)
    else:
        blocks = Block.objects.filter(tid = frames[0].bid)
        return frame(frames, blocks)

def frame_by_eip(request, reip):
    reip = "0x%08x" % int(reip, 0)
    this_block = Block.objects.filter(eip = reip)
    if len(this_block) == 0:
	    return HttpResponse("Invalid eip : " + reip)
    else:
        blocks = Block.objects.filter(tid = this_block[0].tid)
        frames = Frame.objects.filter(eip = reip)
        return frame(frames, blocks)

def frame(frames, blocks):
    content = ""
    content +=  " <!DOCTYPE html> "
    content +=  " <html> "
    content +=  " <head> "
    content +=  "  "
    content +=  simple_css()
    content +=  "  "
    content +=  " </head> "
    content +=  "  "
    content +=  " <body> "
    content +=  "  "
    content +=  "  "
    content +=  " 	<div id=\"raw\"> "

    '''
    RAW HEX VIEW
    '''
    for block in blocks:
        content += "[" + block.eip + "]<br/>"
        #content += block.raw.replace("_|_", "<br/>")
        content += format_raw_hex(block.raw)
	content += "<hr/><br/>"
    content +=  " 	</div> "
    content +=  "  "
    content +=  " 	<div id=\"disasm\"> "

    '''
    DISASMBLY VIEW
    '''
    for block in blocks:
        content += "[" + block.eip + "]<br/>"
        this_disasm = block.disasm.replace("_|_", "<br/>")
        this_disasm = re.sub("(j[a-z]{1,2}|call) (0x[0-9a-fA-F]*)", "\g<1> <a href=\"/frames/\g<2>\">\g<2></a>", this_disasm)
        content += this_disasm
        content += "<hr/><br/>"

    content +=  " 	</div> "
    content +=  "  "
    content +=  "  "
    content +=  "  "
    content +=  " 	<div id=\"reg\"> "

    '''
    REGISTERS VIEW
    '''
    for this_frame in frames:
        content += "eip    : " + this_frame.eip + "<br/>"
        content += "esp    : " + this_frame.esp + "<br/>"
        content += "ebp    : " + this_frame.ebp + "<br/>"
        content += "eax    : " + this_frame.eax + "<br/>"
        content += "ebx    : " + this_frame.ebx + "<br/>"
        content += "ecx    : " + this_frame.ecx + "<br/>"
        content += "edx    : " + this_frame.edx + "<br/>"
        content += "esi    : " + this_frame.esi + "<br/>"
        content += "edi    : " + this_frame.edi + "<br/>"
        content += "<hr/><br/>"

    content +=  " 	</div> "
    content +=  "  "
    content +=  " 	<div id=\"stack\"> "

    '''
    STACK SLOTS VIEW
    '''
    for this_frame in frames:
        content += "stack_0: " + this_frame.stack_0 + "<br/>"
        content += "stack_1: " + this_frame.stack_1 + "<br/>"
        content += "stack_2: " + this_frame.stack_2 + "<br/>"
        content += "stack_3: " + this_frame.stack_3 + "<br/>"
        content += "stack_4: " + this_frame.stack_4 + "<br/>"
        content += "stack_5: " + this_frame.stack_5 + "<br/>"
        content += "stack_6: " + this_frame.stack_6 + "<br/>"
        content += "stack_7: " + this_frame.stack_7 + "<br/>"
        content += "<hr/><br/>"

    content +=  " 	</div> "
    content +=  "  "
    content +=  "  "
    content +=  " </body> "
    content +=  " </html> "

    return HttpResponse(content)

def simple_css():
    css =   " "
    css +=  " <style type=\"text/css\"> "
    css +=  " body{"
    css +=  " background-color: #5A5A5A;"
    css +=  " font-family: monospace;"
    css +=  " }"
    css +=  " div#raw { "
    css +=  " 	background-color:#EEEEEE; "
    css +=  " 	outline:#000000 solid thick; "
    css +=  " 	height:90%; "
    css +=  " 	width:20%; "
    css +=  " 	float:left; "
    css +=  " 	padding:2%;  "
    css +=  " 	margin:1%;  "
    css +=  " 	text-align:left; "
    css +=  " } "
    css +=  " div#disasm { "
    css +=  " 	background-color:#EEEEEE; "
    css +=  " 	outline:#000000 solid thick; "
    css +=  " 	height:90%; "
    css +=  " 	width:25%; "
    css +=  " 	padding:2%;  "
    css +=  " 	margin:1%;  "
    css +=  " 	float:left; "
    css +=  " 	text-align:left; "
    css +=  " } "
    css +=  " div#reg { "
    css +=  " 	background-color:#EEEEEE; "
    css +=  " 	outline:#000000 solid thick; "
    css +=  " 	height:90%; "
    css +=  " 	width:15%; "
    css +=  " 	padding:2%;  "
    css +=  " 	margin:1%;  "
    css +=  " 	float:left; "
    css +=  " 	text-align:left; "
    css +=  " } "
    css +=  " div#stack { "
    css +=  " 	background-color:#EEEEEE; "
    css +=  " 	outline:#000000 solid thick; "
    css +=  " 	height:90%; "
    css +=  " 	width:15%; "
    css +=  " 	padding:2%;  "
    css +=  " 	margin:1%;  "
    css +=  " 	float:left; "
    css +=  " 	text-align:left; "
    css +=  " } "
    css +=  " </style> "
    return css

def html_space():
    return "&nbsp;"

def format_raw_hex(raw):
    raw_hex = ""
    offset = 0
    for hex_line in raw.split("_|_"):
        lens = len(hex_line.split())
        if lens == 0:
            return raw_hex
        if lens <= 8:
            raw_hex += "+%02X:%s<br/>" % (offset, hex_line.strip())
        elif lens <= 16:
            first_slot = hex_line.strip()[0:24]    
            second_slot = hex_line.strip()[24:]
            raw_hex += "+%02X:%s<br/>" % (offset, first_slot.strip())
            raw_hex += "%s%s<br/>" % (html_space() * 4, second_slot.strip())
        elif lens <= 24:
            first_slot = hex_line.strip()[0:24]    
            second_slot = hex_line.strip()[24:48]
            third_slot = hex_line.strip()[48:]
            raw_hex += "+%02X:%s<br/>" % (offset, first_slot.strip())
            raw_hex += "%s%s<br/>" % (html_space() * 4, second_slot.strip())
            raw_hex += "%s%s<br/>" % (html_space() * 4, third_slot.strip())
        else:
            # Are there instructions that occupy 24+ bytes?
            raw_hex += "+%02X:%s<br/>" % (offset, hex_line.strip())

        offset += lens
    return raw_hex
