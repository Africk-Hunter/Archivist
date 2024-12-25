<template>
    <section class="wordBox">
        <div class="wordInfo">
            <h1 class="word">{{ word }}</h1>
            <h2 class="wordType">{{ wordType }}</h2>
        </div>
        <section class="buttons">
            <button @click='previousWord' class="previousWord"><img src="/images/previousButton.svg" alt="Previous Word"
                    class="navigationButton"></button>
            <button @click='nextWord' class="nextWord"><img src="/images/nextButton.svg" alt="Next Word"
                    class="navigationButton"></button>
        </section>
    </section>
</template>

<script>
export default {
    name: 'WordBox',
    methods: {
        previousWord() {
            /* Return the last word */
        },
        nextWord() {
            /* Go to next word */
        }
    },
    props: {
        word: String,
        wordType: String
    }
};
</script>

<style scoped>
.wordBox {
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 25px;
    padding: 2rem 1rem 1rem 1rem;
    border: 1px solid #000;
    width: 20rem;
}

.word {
    margin: 0;
    font-size: 3rem;
    font-weight: 500;
    font-family: 'Montserrat', sans-serif;
}

.wordType {
    margin: 0;
    font-size: 2rem;
    font-weight: 400;
    font-style: italic;
    font-size: 1.5rem;
}

.buttons {
    display: flex;
    justify-content: flex-end;
    width: 100%;
    gap: .3rem
}

.previousWord,
.nextWord {
    display: flex;
    align-items: center;
    height: 2.1rem;
    width: auto;
}

.navigationButton {
    height: 2rem;
    width: auto;
}

.navigationButton:active {
    transform: scale(0.9);
}

@media (min-width: 768px) {

    .wordBox {
        width: 40rem;
        gap: .75rem;
    }

    .word {
        font-size: 5rem;
    }

    .wordType {
        font-size: 2.5rem;
    }
}
</style>