#include<stdio.h>
#include<math.h>

float fun(float t,float y)
{
    float f, t2;
    t2=pow(t, 2);
    f=y-t2+1;
    return f;
}

float g(float t)
{
	float T, yexact;
	T=pow((t+1), 2);
	yexact=T-0.5*exp(t);
	return yexact;
}

float errbd(float t)
{
	float errbound;
	errbound=0.1*(0.5*exp(2)-2)*(exp(t)-1);
	return errbound;
}
			
int main()
{
    float a,b,t,y,h,tem,k,ye,yerr,errorbound;

    a=0.0;
    b=0.5;
    h=0.2;
    tem=2.0;

    t=a;
    y=b;

    printf("\n  t\t  y\n");
    printf("%0.1f\t%0.9f\n",t,y);

    while(t<=tem)
    {
	k=h*fun(t,y);    
	t=t+h;
        y=y+k;
        printf("%0.1f\t%0.9f\n",t,y);
    }

    t=a;
    ye=g(t);

    printf("\n  t\t  ye\n");
    printf("%0.1f\t%0.9f\n",t,ye);

    while(t<=tem)
    {
	    t=t+h;
	    ye=g(t);
	    printf("%0.1f\t%0.9f\n",t,ye);
    }

    printf("\n  t\t\t  abs error of y\n");

    t=a;
    y=b;
    ye=g(t);
    yerr=abs(ye-y);
    printf("%0.1f\t\t%0.9f\n",t,yerr);

    while(t<=tem)
    {
	    k=h*fun(t,y);
            t=t+h;
            y=y+k;
	    ye=g(t);
	    yerr=abs(ye-y);
	    printf("%0.1f\t\t%0.9f\n",t,yerr);
    }

    printf("\n  t\t\t  error bound\n");

    t=a;
    errorbound=errbd(t);
    printf("%0.1f\t\t%0.9f\n",t,errorbound);

    while(t<=tem)
    {
	    t=t+h;
	    errorbound=errbd(t);
	    printf("%0.1f\t\t%0.9f\n",t,errorbound);
    }

    return 0;
} 
