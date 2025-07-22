/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void splice(ListNode* l1, ListNode* l2, ListNode* curr){
        if (!l1 || !l2){
            if (!l1){
                curr -> next = l2;
            }
            else{
                curr -> next = l1; 
            }
            return;
        }
        if (l1 -> val < l2 -> val){
            curr->next = l1;
            splice(l1->next, l2, curr -> next); 
        }
        else{
            curr->next = l2;
            splice(l1, l2 -> next, curr -> next);
        }

    }
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1){
            return list2;
        }
        else if (!list2){
            return list1;
        }
        ListNode* dummy = new ListNode();
        ListNode* current = dummy;
        splice(list1,list2,current);
        return dummy -> next;
    }
};