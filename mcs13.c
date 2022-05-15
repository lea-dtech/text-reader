#include<conio.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct bcastudent
{
    int enrol;
    char name[10];
    int sem;
    int batch;
    char th[50];
    char pr[50];
    char stcode[10];
    char add[150];
}s;

FILE*f1,*f2;
int i,amount,rol;
char chh[150];
int ch;
int b,p;
void addrecord()
{
    f1=fopen("data.txt","ab");
    printf("\nenter the Enrolment No.=");
    scanf("%s",s.enrol);
    fflush(stdin);
    printf("\nenter the Programme name=");
    scanf("%s",s.name);
    printf("\nenter the semester=");
    scanf("%s",&s.sem);
    fflush(stdin);
    printf("\nenter the batch(integer)=");
    scanf("%s",&s.batch);
    fflush(stdin);
    printf("\nenter the Theory Counselling=");
    scanf("%s",s.th);
    printf("\nenter the Practical Counselling=");
    scanf("%s",s.pr);
    fflush(stdin);
    printf("\nenter the study centre code=");
    scanf("%s",s.stcode);
    printf("\nenter the Address: ");
    scanf("%s",s.add);
    fwrite(&s,sizeof(s),1,f1);
    fflush(stdin);
    fclose(f1);
}

void disprecord()
{
    f1=fopen("data.txt","r+b");
    fflush(f1);
    rewind(f1);
    while(fread(&s,sizeof(s),1,f1))
    {
        printf("\nEnrollment=%d\n",s.enrol);
        printf("Programme Name=%s\n",s.name);
        printf("Semester=%d\n",s.sem);
        printf("Study Center=%s\n",s.stcode);
        printf("Address=%s\n",s.add);
        printf("Batch=%d\n",s.batch);
    }
    fclose(f1);
}

void searchrec()
{
    f1=fopen("data.txt","r+b");
    printf("enter the Enrolment NO.: ");
    scanf("%d",&rol);
    rewind(f1);
    while(fread(&s,sizeof(s),1,f1))
    {
        if (rol==s.enrol)
        {
            printf("\nEnrollment=%d\n",s.enrol);
            printf("Programme Name=%s\n",s.name);
            printf("Semester=%d\n",s.sem);
            printf("Study Center=%s\n",s.stcode);
            printf("Address=%s\n",s.add);
            printf("Batch=%d\n",s.batch);
            break;
        }
    }
    if (rol!=s.enrol){
        printf("No Record Founded!");
    }
    fclose(f1);
    fflush(stdin);
}

void searchtheory()
{
    f1=fopen("data.txt","rb+");
    printf("enter the Batch NO.");
    scanf("%d",&b);
    rewind(f1);
    while (fread(&s,sizeof(s),1,f1))
    {
        if(b==s.batch)
        {
            printf("Theory counselling=%s\n",s.th);
            printf("Batch=%d\n",s.batch);
            break;
        }
    }
    fclose(f1);
    if (b!=s.batch){
        printf("No Record Founded!");
    }
    fflush(stdin);
}

void searchpr()
{
    f1=fopen("data.txt","rb+");
    printf("enter the Batch NO.");
    scanf("%d",&p);
    rewind(f1);
    while(fread(&s,sizeof(s),1,f1))
    {
        if (p==s.batch)
        {
            printf("Practical Counselling=%s\n",s.pr);
            printf("Batch=%d\n",s.batch);
            break;
        }
    }
    fclose(f1);
    if (p!=s.batch){
        printf("No Record Founded!");
    }
    fflush(stdin);
}

void chadd()
{
    f1=fopen("data.txt","rb+");
    // clrscr();
    printf("enter the Enroll. NO.");
    scanf("%d",&rol);
    fflush(stdin);
    printf("enter New Address: ");
    gets(chh);
    rewind(f1);
    while(fread(&s,sizeof(s),1,f1))
    {
        if(rol==s.enrol)
        {
            strcpy(s.add,chh);
            printf("Your new address is=%s\n",s.add);
            fseek(f1,-i,SEEK_CUR);
            fwrite(&s,sizeof(s),1,f1);
            fflush(f1);
            break;
        }
    }
    fclose(f1);
    if (rol!=s.enrol){
        printf("Incorrect Enrolment No. %d",rol);
    }
    fflush(stdin);
}

void main()
{
    char chh;
    int choice,isloop;
    i=sizeof(s);
    do
    {
        //clrscr();
        printf("\n0-Add Student Details:");
        printf("\n1-Display student information:");
        printf("\n2-Theory Counselling:");
        printf("\n3-Practical Counselling:");
        printf("\n4-Assignment Submission:");
        printf("\n5-Change Address:");
        printf("\n6-General Quesries:");
        printf("\n7-Quit:");
        printf("\n*********Enter Your Choice**********\n");
        scanf("%d",&choice);
        fflush(stdin);
        switch(choice)
        {
            case 0:
            addrecord();
            break;
            case 1:
            searchrec();
            break;
            case 2:
            searchtheory();
            break;
            case 3:
            searchpr();
            break;
            case 4:
            printf("\n***Assignment Submission Date***\n");
            printf("\nBatch1===>22 March");
            printf("\nBatch2===>23 March");
            printf("\nBatch3===>24 March");
            printf("\nBatch4===>25 March");
            break;
            case 5:
            chadd();
            break;
            case 6:
            disprecord();
            break;
            case 7:
            exit(0);
            break;
            default:
            printf("\nWrong Choice!");
        }
        printf("\nDo you want to continue(y/n): ");
        scanf("%s",&chh);
        isloop=strcmp(&chh,"y");
        //getch();
    } while (isloop==0);
    
}