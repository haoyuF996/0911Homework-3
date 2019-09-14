def main():
    #加载三国人物表
    pre_char_list = open('SanGuoRenWuBiao.txt','r',encoding='UTF-8').readlines()
    #生成词频统计词典 {(姓名，字):频率,......}
    char_fre_dict = {}#初始化
    for line in pre_char_list:
        if line!='':#排除空行
            words = line.split(' ')
            #关联人物姓名和字
            count=0
            while count<len(words):#文本顺序为: 姓名 字 姓名 字.....
                #删除空值
                while words[count] == '':
                    words.remove('')
                if (-1)**count == 1:
                    ming = words[count]#抓取姓名
                else:
                    zi = words[count]#抓取字
                    char_fre_dict[(ming,zi)] = 0#初始数据添加入词典
                count+=1

    import jieba
    #结巴分词
    word_list = jieba.lcut(open('SanGuoYanYi.txt','r',encoding='UTF-8').read())
    #统计词频
    for word in word_list:
        for char in char_fre_dict:
            if char[0]==word or char[1]==word:
                char_fre_dict[char] += 1
    #生成姓名-频率词典 {姓名:频率,......}
    fre_dict = {}
    for char in char_fre_dict:
        fre_dict[char[0]] = char_fre_dict[char]#只包括姓名
    #生成词云
    from wordcloud import WordCloud
    wc = WordCloud(font_path='HYQiHei-25J.ttf',background_color="white")#font_path中文字体
    wc.generate_from_frequencies(fre_dict)#使用频率词云无需排序
    wc.to_file("SanGuo.png")#保存图片

if __name__ == "__main__":
    #文件目录下需包含SanGuoYanYi.txt, HYQiHei-25J.ttf, SanGuoRenWuBiao.txt
    main()