#include <stdio.h>
#include <string.h>
#include <stdlib.h>


typedef struct{
    char name[100];
    int age;
}Person;

void merge(Person a[], int l, int m, int r, int mode){
    int n1=m-l+1;
    int n2=r-m;
    Person L[n1];
    Person R[n2];
    int i, j;
    for ( i=0; i<n1; i++){
        L[i]=a[l+i];
    }
    for(j=0; j<n2; j++){
        R[j]=a[m+1+j];
    }
    i=0;
     j=0;
    int k=l;
    while((i<n1)&&(j<n2)){
        if (mode==0){
            if (L[i].age<=R[j].age){
                a[k]=L[i];
                i++;
            }else{
                a[k]=R[j];
                j++;
            }
        }else{
            if (strcmp(L[i].name, R[j].name)<0){
                a[k]=L[i];
                i++;
            }else{
                a[k]=R[j];
                j++;
            }
        }
        k++;
    }
    while(i<n1){
        a[k]=L[i];
        i++;
        k++;
    }
    while(j<n2){
        a[k]=R[j];
        j++;
        k++;
    }
}

void mergeSort(Person a[], int l, int r, int mode){
    if(l<r){
        int m=l+(r-l)/2;
        mergeSort(a, l, m, mode);
        mergeSort(a, m+1, r, mode);
        merge(a, l, m, r, mode);
    }
}

void displayPerson(Person* p, int number){
    int i;
	for(i=0; i<number; i++){
        printf("%d. %s, ", i+1, p[i].name);
        printf("%d \n", p[i].age);
    }
}


int main(){

    int number;
    
    printf("Enter number of students: ");
    scanf("%d", &number);
    printf("\n");
    
    Person p[number];
	int i;
    for(i=0; i<number; i++){
        getchar();
        printf("Enter student %d's name: ", i+1);
        fgets(p[i].name, sizeof(p[i].name), stdin);
        p[i].name[strcspn(p[i].name, "\n")]=0;
        
        printf("Enter student %d's age: ", i+1);
        scanf("%d", &p[i].age);
    }

    printf("\n");
    mergeSort(p, 0, number-1, 0);
    printf("CLASS LIST (Sorted by Age): \n");
    displayPerson(p, number);
    
    printf("\n");
    mergeSort(p, 0, number-1, 1);
    printf("CLASS LIST (Sorted by Name): \n");
    displayPerson(p, number);

    
    
    return 0;
}
