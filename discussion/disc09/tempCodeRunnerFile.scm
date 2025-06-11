(define (pair-up s)
        (if (<= (length s) 3)
            (list s)
            (cons (list (car s) (car (cdr s))) (pair-up (cdr (cdr s)))))

        )

    (expect (pair-up '(3 4 5 6 7 8)) ((3 4) (5 6) (7 8)) )
    (expect (pair-up '(3 4 5 6 7 8 9)) ((3 4) (5 6) (7 8 9)) )