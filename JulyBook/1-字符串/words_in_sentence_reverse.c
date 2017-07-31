#include <stdio.h>
#include <string.h>
int reverse_in_place(int, int, char[]);

void reverse(char sentence[]){
  printf("%s\n", sentence);
  int len = strlen(sentence);
  int start = 0;
  //把空格分割的单词进行反转
  for(int index=0; index < len; index++){
    if(sentence[index] == ' '){
      start = reverse_in_place(start, index-1, sentence);    
    }
  }
  //最后一个单词进行反转
  reverse_in_place(start, len-1, sentence);
  
  //二次反转整个句子
  reverse_in_place(0, len-1, sentence);
  printf("%s\n", sentence);
}

/**
 * 原地反转start，end之间的字符
 */
int reverse_in_place(int start, int end, char str[]){
  int middle = start + ((end - start) >> 1);
  //printf("start:%d, end:%d, middle:%d, %s\n",start, end, middle, str);
  if(middle < end){
    for(int i=start; i <= middle; i++){
      int tail = end - i + start;
      if(i < tail){
        //printf("%d, %d\n",i,tail);
        char temp = str[i];
        str[i] = str[tail];
        str[tail] = temp;
      }
    }
  }
  return end + 2;
}

int main(int argc, char *argv[]){
  char s[] = "I am a programmer."; 
  reverse(s);
}
