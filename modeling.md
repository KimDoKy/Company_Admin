- entity: company_system (부서) / member relation MTO
 - attribute: system_name(조직명/PK/char), member(조직원/Foreign/member table과 OneToMany)

- entity: member (조직원) / company_system relation OTM
 - attribute: 회원번호(PK/int), id(아이디/char), password(패스워드/char), name(이름/char), birth(생년월일/date), number(자리번호/num), phone(연락처/num), email(이메일/text), active(활성화 상태/bool)

- entity: product (상품) / contract relation MTM
 - attribute: prod_code(pk/int), prod_name(text/상품명), prod__description(text/상품설명), active(bool/활성화여부)
 - 특이사항: 상품명이 text이다. order의 특징은 글자수 제한없이 작명한다.

- entity: contract (계약) / product relation MTM / payment relation OTO
 - attribute: cont_code(pk/계약번호/int), comp_ceo(대표자 성명/char), comp_name(상호명/char), comp_num(사업자번호/int), comp_biz(업태/char), comp_cate(업종/char), comp_post(우편번호/int), comp_addr(주소/text), comp_phone(전화번호/int), comp_phone2(휴대폰번호/int), comp_fax(팩스번호/int), comp_email(이메일/text), comp_person(담당자/char), comp_url(홈페이지주소/text)

- entity: payment (결제) / contract relation OneToOne / card, bank relation MTO
 - attribute: pay_type(Foreign)

- entity: card (카드결제) / payment relation OTM
 - attribute: cont_money(결제금액/int), card_comp(카드사/char), card_num(카드번호/int), card_life(유효기간/date), card_con_day(결제일/date), card_plan(할부기간/int), card_calc(정산일/date), card_calc_money(정산금/int)

- entity: bank (계좌이체/무통장입금) / payment relation OTM
 - attribute: bank_money(결제금액/int), bank_name(입금은행/char), bank_int_name(입금자명/char), bank_bill(계산서 발행일/date), bank_bill_bool(계산서 발행 여부/bool)

