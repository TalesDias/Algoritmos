#!/usr/bin/env stack
{- stack script
   --resolver lts-17.5
-}

import System.CPUTime ( getCPUTime )
import Control.DeepSeq ( NFData, deepseq ) 
import Control.Monad ( replicateM )
import Data.List ( partition )

main :: IO()
main = do
   contents <- readFile "amostra"

   let lista = map (\x -> read x ::Integer ) (words contents )
   print "loaded"
   
   print $ last lista
   print "inMemory"
   
   totTime <- sum <$> replicateM 10 (benchmark quickSort lista)
   print totTime

   (print . picoToSeconds . fromIntegral) (div totTime 10)

   return ()




benchmark :: (Ord a, NFData a) => ([a] -> [a]) -> [a] -> IO Integer
benchmark func input = do
                     start <- getCPUTime
                     let xs = func input
                     end <- xs `deepseq` getCPUTime
                     return (end - start)


picoToSeconds :: Integer -> Double
picoToSeconds = (/10^9) . fromIntegral . truncate . (/1000) . fromIntegral

isSorted :: Ord a => [a] -> Bool
isSorted [] = True
isSorted [x] = True
isSorted (x:y:xs) = x <= y && isSorted (y:xs)

quickSort :: Ord a => [a] -> [a]
quickSort [ ] = [ ]
quickSort [x] = [x]
quickSort (x:xs) =  quickSort menores ++ [x] ++ quickSort maiores
   where (menores, maiores) = partition (<x) xs

mergeSort :: Ord a => [a] -> [a]
mergeSort [ ] = [ ]
mergeSort [x] = [x]
mergeSort xs = merge (mergeSort (take sz xs)) (mergeSort (drop sz xs))
   where 
      sz = div (length xs) 2
      merge [] ys = ys
      merge xs [] = xs
      merge (x:xs) (y:ys) = 
         if x > y 
            then y:merge (x:xs) ys 
            else x:merge (y:ys) xs
