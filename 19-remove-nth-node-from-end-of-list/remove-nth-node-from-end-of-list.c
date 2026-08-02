/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode* first = head;
    struct ListNode* last = head;
    for(int i=0; i<n; i++){
        first = first -> next;
    }
    if(first == NULL){
        head = head -> next;
        return head;
    }
    while (first ->next != NULL){
        first = first-> next;
        last = last -> next;
    }
    last ->next = last -> next -> next;
    return head;
}