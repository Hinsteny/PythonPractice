from spider.common.FileUtils import write_content_to_file

if __name__ == '__main__':
    filePath = "E:/data/python/test.txt"
    content = "Hello World!"
    write_content_to_file(filePath, content)