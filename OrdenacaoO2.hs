#!/usr/bin/env stack
{- stack
   script
   --resolver lts-17.5
-}


-- Feitos sem proposito de teste

module OrdenacaoO2 where

import Data.List (foldl')

main :: IO ()
main = do
    let list = [4,65,43,2,5,6,8,43,7,9,8,64,4,321,5,67,8,7,5,32,43,74,3]
    
    print "SelectionSort"
    print $ selectionSort list

    print "InsertionSort"
    print $ insertionSort list

    print "BubbleSort"
    print $ bubbleSort list


selectionSort :: Ord a => [a] -> [a]
selectionSort [] = [] 
selectionSort xs = minimum xs : selectionSort (delete (minimum xs) xs)

insertionSort :: Ord a => [a] -> [a]
insertionSort = foldl' insert []
    where 
        insert [] el = [el]
        insert (x:xs) el = if x >= el then el:x:xs else x:insert xs el
 
bubbleSort :: Ord a => [a] -> [a]
bubbleSort [] = []
bubbleSort xs = (bubbleSort . init) ys ++ [last ys]
    where 
        ys = bubble xs
        bubble [x] = [x]
        bubble (x:y:xs) = if x < y then x:bubble (y:xs) else y:bubble (x:xs)


-- Eu sei que Data.List implementa a função
-- Mas quis pensar em como eu a implementaria
delete :: Eq a => a -> [a] -> [a]
delete _ [] = []
delete y (x:xs) 
    | y == x = xs
    | otherwise = x : delete y xs
