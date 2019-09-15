def main():
    #加载三国人物表
    pre_char_list = ('\n'.join(open('SanGuoRenWuBiao.txt','r',encoding='UTF-8').read().split(' '))).split('\n')#消除空格和换行符
    #生成词频统计词典 {(姓名，字):频率,......}
    char_fre_dict,count = {},0#初始化
    #关联人物姓名和字
    for i,word in enumerate(pre_char_list):#文本顺序为: 姓名 字 姓名 字.....
        if word!='':#排除空字符
            if (-1)**count == 1:
                ming = word#抓取姓名
            else:
                zi = word#抓取字
                char_fre_dict[(ming,zi)] = 0#初始数据添加入词典
            count+=1
    #结巴分词
    import jieba
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