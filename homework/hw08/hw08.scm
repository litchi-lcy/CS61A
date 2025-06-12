(define (ascending? s)
     (or (null? s)
     (null? (cdr s))
     (and (ascending? (cdr s)) 
      (or (< (car s) (car (cdr s))) (= (car s) (car (cdr s)))))))
       

(define (my-filter pred s) 
    (if (null? s) 
        ()
        (if (pred (car s))
            (cons (car s) (my-filter pred (cdr s))) 
            (my-filter pred (cdr s)))))


(define (interleave lst1 lst2) 
    (if (null? lst1) 
        lst2
        (cons (car lst1) (interleave lst2 (cdr lst1)))))




(define (no-repeats s) 
    (if (or (null? s) (null? (cdr s)))
        s 
       (cons (car s) (filter (lambda (x) (not (= (car s) x))) (no-repeats (cdr s))))))


;(define (no-repeats s)
;    (if (or (null? s) (null? (cdr s)))
;        s 
        
 ;       (if (eq? (car s) (car(cdr s))) (no-repeats (cdr s)) (cons (car s) (no-repeats (cdr s))))))
;(define (no-repeats s) (filter (lambda () (not (= (no-repeats t) (cons (car t) (no-repeats (cdr t)))))) s))