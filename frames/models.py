from django.db import models, connection

#class FrameManager(models.Manager):

#    def create_in_bulk(self, values):
#        base_sql = "INSERT INTO frames_frame (d, gid, bid, eip, esp, ebp, eax, ebx, ecx, edx, esi, edi, stack_0, stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7) VALUES "
#        values_sql = []
#        values_data = []
#
#        for value_list in values:
#            placeholders = ['%s' for i in range(len(value_list))]
#            values_sql.append("(%s)" % ','.join(placeholders))
#            values_data.extend(value_list)
#
#        sql = '%s%s' % (base_sql, ', '.join(values_sql))
#
#        curs = connection.cursor()
#        curs.execute(sql, values_data)

class Frame(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    gid = models.CharField(max_length=10)
    bid = models.CharField(max_length=10)
    eip = models.CharField(max_length=10)
    esp = models.CharField(max_length=10)
    ebp = models.CharField(max_length=10)
    eax = models.CharField(max_length=10)
    ebx = models.CharField(max_length=10)
    ecx = models.CharField(max_length=10)
    edx = models.CharField(max_length=10)
    esi = models.CharField(max_length=10)
    edi = models.CharField(max_length=10)
    stack_0 = models.CharField(max_length=10)
    stack_1 = models.CharField(max_length=10)
    stack_2 = models.CharField(max_length=10)
    stack_3 = models.CharField(max_length=10)
    stack_4 = models.CharField(max_length=10)
    stack_5 = models.CharField(max_length=10)
    stack_6 = models.CharField(max_length=10)
    stack_7 = models.CharField(max_length=10)

#    objects = FrameManager()

#class BlockManager(models.Manager):
#
#    def create_in_bulk(self, values):
#        base_sql = "INSERT INTO frames_block (id, tid, raw, disasm) VALUES "
#        values_sql = []
#        values_data = []
#
#        for value_list in values:
#            placeholders = ['%s' for i in range(len(value_list))]
#            values_sql.append("(%s)" % ','.join(placeholders))
#            values_data.extend(value_list)
#
#        sql = '%s%s' % (base_sql, ', '.join(values_sql))
#
#        curs = connection.cursor()
#        curs.execute(sql, values_data)

class Block(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    tid = models.CharField(max_length=10)
    eip = models.CharField(max_length=10)
    raw = models.CharField(max_length=512)
    disasm = models.CharField(max_length=512)
