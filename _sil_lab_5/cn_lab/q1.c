#include <stdio.h>
#include <stdlib.h>
struct student
{
  char name[20], branch[20];
  int regd, sem;
};
void add(struct student s1);
void search(struct student s1);
void displayAll();

int main()
{
  int ch, i = 0;
  struct student st, stud;
  while (1)
  {
    printf("\n1:To add new record\t2: To search a record\t3: To display all records\tEnter 4 to Exit\n");
    scanf("%d", &ch);

    switch (ch)
    {
    case 1:
      printf("\n Enter the student name:- ");
      scanf(" %s", st.name);
      printf("\n Enter the student branch:- ");
      scanf(" %s", st.branch);
      printf("\n Enter the student Registration number:- ");
      scanf("%d", &st.regd);
      printf("\n Enter semester:- ");
      scanf("%d", &st.sem);
      add(st);
      break;
    case 2:
      printf("\nEnter the registration number\n");
      scanf("%d", &stud.regd);
      search(stud);
      break;
    case 3:
      displayAll();
      break;
    case 4:
      exit(0);
    }
  }
}

void add(struct student s1)
{
  static int i = 0;
  struct student stu[400];
  stu[i] = s1;
  FILE *fptr;
  fptr = fopen("student_file.txt", "a");

  if (fptr == NULL)
  {
    printf("Error!");
    exit(1);
  }
  fwrite(&stu[i], sizeof(struct student), 1, fptr);
  if (fwrite != 0)
  {
    printf("Saved successfully ! \n");
    i++;
  }
  else
    printf("Error in writing file !\n");

  fclose(fptr);
}
void search(struct student s1)
{
  FILE *infile;
  struct student st;
  infile = fopen("student_file.txt", "r");
  if (infile == NULL)
  {
    fprintf(infile, "\nError opening file\n");
    exit(1);
  }
  while (fread(&st, sizeof(struct student), 1, infile))
  {
    if (st.regd == s1.regd)
    {
      printf("Name = %s \n Branch = %s \n Registration no= %d \n Semester= %d \n", st.name, st.branch, st.regd, st.sem);
    }
  }

  fclose(infile);
}
void displayAll()
{
  FILE *infile;
  struct student st;
  infile = fopen("student_file.txt", "r");
  if (infile == NULL)
  {
    fprintf(stderr, "\nError opening file\n");
    exit(1);
  }
  while (fread(&st, sizeof(struct student), 1, infile))
    printf("Name = %s\nBranch = %s\nRegistration no= %d\nSemester= %d\n", st.name, st.branch, st.regd, st.sem);

  fclose(infile);
}
