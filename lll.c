#include<stdio.h>
#include<stdlib.h>

typedef struct node{
    int data;
    struct node* next;
}node;

node* create(int data){
    node* node1 = (node*)malloc(sizeof(node1));
    node1->data = data;
    node1->next = NULL;
    return node1;
}
node* add(node* head, int data){
    node* node1 = create(data);
    if(head == NULL){
        return node1;
    }
    node* temp = head;
    while(temp->next!=NULL){
        temp = temp->next;
    }
    temp->next = node1;
    return head;
}
node* del(node* head, int data){
    if(head == NULL){
        return NULL;
    }
    if(data == head->data){
        node* temp = head;
        head = head->next;
        free(temp);
        return head;
    }
    node* temp = head;
    while(temp->next != NULL && temp->next->data != data){
        temp = temp->next;
    }
    node* del = temp->next;
    temp->next = del->next;
    free(del);
    return temp;
}
void display(node* head){
    node* temp = head;
    printf("Linked list: ");
    while(temp!=NULL){
        printf("%d->",temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}
int main(){
    struct node* head = NULL;
    head = create(10);
    head = add(head,20);
    head = add(head,30);
    display(head);
    head = del(head,30);
    display(head);
}