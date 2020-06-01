from django.db import models

# Create your models here.

class Label(models.Model):

    label_id = models.AutoField('序号',primary_key=True)
    label_name = models.CharField('分类列表',max_length=10)
    def __str__(self):
        return self.label_name

class Song(models.Model):

    song_id = models.AutoField('序号',primary_key=True)
    song_name = models.CharField('歌名',max_length=50)
    song_singer = models.CharField('歌手',max_length=50)
    song_time = models.CharField('时长',max_length=10)
    song_ablum = models.CharField('专辑',max_length=50)
    song_language = models.CharField('语种',max_length=20)
    song_type = models.CharField('类型',max_length=20)
    song_release = models.CharField('发行时间',max_length=20)
    song_img = models.CharField('歌曲图片',max_length=20)
    song_lyrics = models.CharField('歌词',max_length=50,default='暂无歌曲')
    song_file = models.CharField('歌曲文件',max_length=50)
    label = models.ForeignKey(Label,on_delete=models.CASCADE,verbose_name='歌曲分类')

    def __str__(self):
        return self.song_name

class Dynamic(models.Model):

    dynamic_plays = models.AutoField('序号',primary_key=True)
    song = models.ForeignKey(Song,on_delete=models.CASCADE,verbose_name='歌名')

    dynamic_plays = models.IntegerField('播放次数')
    dynamic_search = models.IntegerField('搜索次数')
    dynamic_down = models.IntegerField('下载次数')

class Comment(models.Model):
    comment_id = models.AutoField('序号',primary_key=True)
    comment_text = models.CharField('评论',max_length=500)
    comment_user = models.CharField('评论用户',max_length=20)
    song = models.ForeignKey(Song,on_delete=models.CASCADE,verbose_name='歌名')
    comment_date = models.CharField('评论时间',max_length=50)
    pass

    pass
