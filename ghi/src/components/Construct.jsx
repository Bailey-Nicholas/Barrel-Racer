function Construct(props) {
    if (!props.info) {
        return <p>Loading...</p>
    }

    return (
        <>
            <h1>Under construction</h1>
            <img src="/underconstruction.JPEG" alt="Under Construction" />
        </>
    )
}

export default Construct
