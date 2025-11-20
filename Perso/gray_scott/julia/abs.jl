function max_valeur_absolue(nombres)
    max_abs = 0
    for n in nombres
        if abs(n) > max_abs
            max_abs = abs(n)
        end
    end
    return max_abs
end

# syntaxe concise
max_valeur_absolue(nombres) = maximum(abs.(nombres))

println(max_valeur_absolue([3, -7, -1, 5]))  # Affiche 7