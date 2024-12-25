<template>
    <section class="descriptionContainer">
        <p class="pronunciation">{{ pronunciation }}</p>
        <p class="definition">{{ definition }}</p>
    </section>
</template>

<script>
export default {
    name: 'DescriptionContainer',
    props: {
        pronunciation: String,
        definition: String
    }
};
</script>

<style scoped>
.desctiptionContainer {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
    margin-top: 1rem;
}

p {
    margin: 0;
}

.pronunciation {
    font-size: 1.5rem;
    font-weight: 400;
}

.definition {
    font-size: 1.6rem;
    font-weight: 400;
}

@media (min-width: 768px) {
    .pronunciation {
        font-size: 2rem;
    }

    .definition {
        font-size: 2.25rem;
    }
}
</style>