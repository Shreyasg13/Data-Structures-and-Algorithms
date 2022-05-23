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
    ListNode* reverseList(ListNode* head) {
          ListNode* ans;
        if(head==nullptr||head->next==nullptr )
            return head;
        ans=reverseList(head->next);
        
        head->next->next=head;
        head->next=NULL;
        return ans;
        
     /*   
    ListNode*prev= new ListNode();
	ListNode*current= new ListNode();
	ListNode* next= new ListNode();
	
	current = head;
	prev=NULL;
	
	
	while(current != NULL)
	{
		
	next=current->next;
	current->next=prev;
	prev=current;
	current=next;
			
	}
	 head=prev;
        
    return head;*/
    }
};