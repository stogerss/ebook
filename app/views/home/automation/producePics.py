import sys
import os

def main(args):
    video = args[0]
    transcript = args[1]
    f = open(transcript, 'r')
    saveTo = video[:-4] + '.html'
    saveHTML = open('../'+saveTo, 'w')
    
    html = '<link href=\'../../assets/stylesheets/application.css\' rel=\'stylesheet\'>'
    
    html += '<br> <div class="header"> <div class=\'ChapterHeader\'> <a href=\'\'> <img class=\'nav-left\' src=\'../../assets/images/left_arrow.png\'></a> <span class=\'ChapterWording\'> Chapter 8: Web Security </span> <a href=\'\'> <img class=\'nav-right\' src=\'../../assets/images/right_arrow.png\'></a> </div> </div> <br>'
    
    html += '<div class=\'content\'> <div class="index"> <div class="l0">Sections </div> <hr class="blue"> <hr class="blue"> <a href="#Introduction"> <div class="l1">Introduction</div> </a> <a href="#Http Protocol"> <div class="l1">Http Protocol</div> </a> <a href="#Rendering"> <div class="l1">Rendering</div> </a> <a href="#Isolation"> <div class="l1">Isolation</div> </a> <a href="communication.html"> <div class="l1">Communication</div> </a> <a href="#Navigation"> <div class="l1">Navigation</div> </a> <a href="#Cookies"> <div class="l1">Cookies</div> </a> <a href="#Security UI"> <div class="l1">Security UI</div> </a> <a href="#Frames"> <div class="l1">Frames</div> </a> </div> <div class=\'content-wrapper\'> <div class=\'introduction\'> <div class=\'title\'>Chapter 8: Web Security</div> <p>In this chapter we will talk about Web Security.</p> <div class=\'section-title\'>Section 8.1: Introduction</div>'
    
    saveHTML.write(html)
    
    for line in f:
        if(line[0] == '['):
#os.system
            if(line[:-1] == '[00:00:00]'):
                os.system('ffmpeg -i communication.mp4 -ss ' + line[1:-4] + '16 -f image2 -vframes 1 out/out' + line[1:-4] + '16.png')
                html = '<img class="inline" src=automation/out/out'+ line[1:-4] +'16.png>'
                
                
                saveHTML.write(html + '\n')
            
            elif(not(line[1] == 'E')):
                os.system('ffmpeg -i communication.mp4 -ss ' + line[1:-2] + ' -f image2 -vframes 1 out/out' + line[1:-2] + '.png')
                html = '<img class="inline" src=automation/out/out'+ line[1:-2] +'.png>'
    
                saveHTML.write(html + '\n')
            else:
                print saveHTML
        elif len(line) > 1:
            
            html = '<p class="txt">' + line.replace('\'', '&#39;') + '</p>'
            #print line
            saveHTML.write(html + '\n')
        
    saveHTML.write('<br> <br> <br> <br> <br> <img class="inline-t" src="../../assets/images/messages_sent.png">')
    saveHTML.write('</div> </div> </div> </div>')
    



if __name__ == '__main__':
    args = sys.argv[1:]
    try:
        main(args)
    except IOError:
        print 'IOError: ' + str(IOError)