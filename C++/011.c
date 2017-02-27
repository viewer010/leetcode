#include<stdio.h>
#include<iostream>
using namespace std;
int maxArea(int* ,int);
int maxArea(int* height, int heightSize) {
    int i=0,j=0;
    int temp=0;
    int max=0;
    int area=0;
    int h1=0,h2=0;
    for(temp=0;temp<heightSize;temp++)
    {
        h2=*(height+temp);
        //printf("%d",h2);
        for(i=0;i<heightSize;i++)
        {
            //h3=*(height+i);
            if ( *(height+i) >=h2)
            {
                for(j=heightSize-1;j>i;j--)
                {
                    h1=*(height+j);
                    if (h1>=h2)
                    {
                        area=(j-i)*h2;
                        cout<<h1<<' '<<h2<<' '<<area<<endl;
                        if (area>max)
                            max=area;
                        break;
                    }
                }
                break;
            }
        }
    }
    return max;
}

int main(){
    int height[]={1,2,3,4};
    int result = maxArea(height, 4 );
    cout<<result<<endl;
    
}
