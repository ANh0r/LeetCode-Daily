/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        ListNode *pst = head;
        ListNode *last = NULL;
        int count = 0;
        while(pst != NULL){
            ++count;
            last = pst;
            pst = pst->next;
        }
        if(count == 0){
            return head;
        }
        int actual = k % count;
        last -> next = head;
        pst = head;
        for(int i = 0;i < count - actual - 1;++i){
            pst = pst->next;
        }
        head = pst->next;
        pst->next = NULL;
        return head;
    }
};