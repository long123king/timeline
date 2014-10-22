import os,sys
import csv
import models

def import_frame(filename):
	frames = []
	frame_reader = csv.reader(open(filename))
	for id, bid, eip, esp, ebp, eax, ebx, ecx, edx, esi, edi, stack_0, stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7 in frame_reader:
    		#frame = models.Frame(id, bid, eip, esp, ebp, eax, ebx, ecx, edx, esi, edi, stack_0, stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7)
    		#frame.save()
		frames.append((id, bid, eip, esp, ebp, eax, ebx, ecx, edx, esi, edi, stack_0, stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7))
	models.Frame.objects.create_in_bulk(frames)

def import_block(filename):
	blocks = []
	block_reader = csv.reader(open(filename))
	for id, tid, raw, disasm in block_reader:
		#block = models.Block(id, tid, raw, disasm)
		#block.save()
		blocks.append((id, tid, raw, disasm))
	models.Block.objects.create_in_bulk(blocks)
		

